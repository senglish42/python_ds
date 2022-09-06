echo '"id", "created_at", "name", "has_test", "alternate_url"'
jq --raw-output '.items[] | [.id, .created_at, .name, .has_test, .alternate_url] | @csv'