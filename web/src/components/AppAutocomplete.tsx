import type { AutocompleteOption } from "@/lib/autocompleteOption";
import type { AutocompleteEntry } from "@/lib/generated";
import {
  autocompleteSearchOptions,
  autocompleteSingleOptions,
} from "@/lib/generated/@tanstack/react-query.gen";
import { useQuery } from "@tanstack/react-query";
import { Select } from "antd";
import React, { useState } from "react";
import { useDebounce } from "use-debounce";

interface AppAutocompleteProps {
  value?: number | null;
  onChange?: (value: number | null) => void;
  entityName: AutocompleteOption;
}

function transformAutocompleteResponse({ id, label }: AutocompleteEntry) {
  return { value: id, label };
}

export default function AppAutocomplete({
  value,
  onChange,
  entityName,

  ...props
}: AppAutocompleteProps & React.ComponentProps<typeof Select>) {
  const [hasBeenFocused, setHasBeenFocused] = useState(false);
  const [searchText, setSearchText] = useState("");
  const [debouncedSearchText] = useDebounce(searchText, 300);

  const { data, isFetching } = useQuery({
    ...autocompleteSearchOptions({
      path: { name: entityName },
      query: { search: debouncedSearchText, take: 50, skip: 0 },
    }),
    enabled: hasBeenFocused,
  });

  const { data: selectedOption, isFetching: isFetchingSelectedOption } =
    useQuery({
      ...autocompleteSingleOptions({
        path: { name: entityName, id: value! },
      }),
      enabled: value != null && !data?.some((x) => x.id === value),
    });

  const options = data?.map(transformAutocompleteResponse) ?? [];
  if (selectedOption && !options.find((o) => o.value === selectedOption.id))
    options.unshift(transformAutocompleteResponse(selectedOption));

  return (
    <Select
      {...props}
      value={value ?? null}
      onChange={onChange ?? ((_) => {})}
      showSearch={{ filterOption: false, onSearch: setSearchText }}
      options={options}
      loading={isFetching || isFetchingSelectedOption}
      onFocus={(...args) => {
        setHasBeenFocused(true);
        if (props.onFocus) props.onFocus(...args);
      }}
    />
  );
}
