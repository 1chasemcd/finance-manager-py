import {
  lookupImportDefOptions,
  searchImportDefsQueryKey,
  updateImportDefMutation,
} from "@/lib/generated/@tanstack/react-query.gen";
import ImportDefModifyForm from "./ImportDefModifyForm";
import EntityUpdateForm from "@/components/EntityForm/EntityUpdateForm";
import type { WriteImportDef } from "@/lib/generated";

export default function ImportDefUpdate() {
  return (
    <EntityUpdateForm
      title="Edit Category"
      lookupEntityOptions={lookupImportDefOptions}
      updateEntityMutation={updateImportDefMutation}
      dataTransform={(x) => x as WriteImportDef}
      toInvalidate={[searchImportDefsQueryKey()]}
    >
      <ImportDefModifyForm />
    </EntityUpdateForm>
  );
}
