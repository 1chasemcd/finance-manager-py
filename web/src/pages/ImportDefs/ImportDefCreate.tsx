import EntityCreateForm from "@/components/EntityForm/EntityCreateForm";
import {
  searchImportDefsQueryKey,
  createImportDefMutation,
} from "@/lib/generated/@tanstack/react-query.gen";
import ImportDefModifyForm from "./ImportDefModifyForm";

export default function ImportDefCreate() {
  return (
    <EntityCreateForm
      title="Add Category"
      createEntityMutation={createImportDefMutation}
      toInvalidate={[searchImportDefsQueryKey()]}
    >
      <ImportDefModifyForm />
    </EntityCreateForm>
  );
}
