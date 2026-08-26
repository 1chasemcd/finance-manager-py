import type {
  HttpValidationError,
  ProblemDetails,
  ValidationError,
} from "@/lib/generated";
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
  form.setFields(groupValidations(problem.detail));
}

function joinFieldValidationErrors(problem: HttpValidationError) {
  return (problem.detail ?? [])
    .flatMap((err) => `${createPath(err.loc)}: ${err.msg}`)
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

function groupValidations(details: ValidationError[]) {
  const grouped = details.reduce<Record<string, string[]>>((acc, error) => {
    (acc[createPath(error.loc)] ??= []).push(error.msg);
    return acc;
  }, {});

  return Object.entries(grouped).map(([name, errors]) => ({
    name,
    errors,
  }));
}

function createPath(loc: (string | number)[]) {
  return loc.slice(1).join(".");
}
