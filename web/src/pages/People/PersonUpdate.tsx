import {
  lookupPersonOptions,
  searchPeopleQueryKey,
  updatePersonMutation,
} from "@/lib/generated/@tanstack/react-query.gen";
import PersonModifyShared from "./PersonModifyShared";
import EntityUpdateForm from "@/components/EntityForm/EntityUpdateForm";
import type { WritePerson } from "@/lib/generated";

export default function PersonUpdate() {
  return (
    <EntityUpdateForm
      title="Edit Person"
      lookupEntityOptions={lookupPersonOptions}
      updateEntityMutation={updatePersonMutation}
      dataTransform={(x) => x as WritePerson}
      toInvalidate={[searchPeopleQueryKey()]}
    >
      <PersonModifyShared />
    </EntityUpdateForm>
  );
}
