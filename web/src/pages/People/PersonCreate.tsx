import EntityCreateForm from "@/components/EntityForm/EntityCreateForm";
import {
  searchPeopleQueryKey,
  createPersonMutation,
} from "@/lib/generated/@tanstack/react-query.gen";
import PersonModifyShared from "./PersonModifyShared";

export default function PersonCreate() {
  return (
    <EntityCreateForm
      title="Add Person"
      createEntityMutation={createPersonMutation}
      toInvalidate={[searchPeopleQueryKey()]}
    >
      <PersonModifyShared />
    </EntityCreateForm>
  );
}
