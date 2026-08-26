import type { HttpValidationError, ProblemDetails } from "@/lib/generated";
import { App, type FormInstance } from "antd";
import { useCallback } from "react";

const DEFAULT_TITLE = "Error";
const DEFAULT_CONTENT = "An unexpected problem occurred.";

export default function useErrorHandler() {
  const { modal } = App.useApp();

  return useCallback(
    (error: unknown, form?: FormInstance) => {
      let modalError = { title: DEFAULT_TITLE, content: DEFAULT_CONTENT };
      if (isHttpValidationError(error)) {
        if (form) return handleValidationFormErrors(form, error);
        modalError.title = "Validation Errors";
        if (error.detail) modalError.content = joinFieldValidationErrors(error);
      }
      if (isProblemDetails(error)) {
        if (error.title) modalError.title = error.title;
        if (error.detail) modalError.content = error.detail;
      }
      modal.error(modalError);
    },
    [modal],
  );
}

function handleValidationFormErrors(
  form: FormInstance,
  problem: HttpValidationError,
) {
  if (!problem.detail) return;
  form.setFields(
    problem.detail.map((err) => ({
      name: "",
      errors: [err.msg],
    })),
  );
}

function joinFieldValidationErrors(problem: HttpValidationError) {
  return (problem.detail ?? [])
    .flatMap((err) => `${err.loc}: ${err.msg}`)
    .join("\n");
}

function isHttpValidationError(error: unknown): error is HttpValidationError {
  return (
    typeof error === "object" &&
    error !== null &&
    Object.hasOwn(error, "detail")
  );
}

function isProblemDetails(error: unknown): error is ProblemDetails {
  return (
    typeof error === "object" &&
    error !== null &&
    (Object.hasOwn(error, "title") || Object.hasOwn(error, "detail"))
  );
}
