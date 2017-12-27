# steam-organisation
A bunch of Python utilities to Make Your Life Easier™

#### sort_keys.py
##### This wonderful little thing helps you sort your spare Steam keys.
```
manpage:

Usage: python sort_keys.py <sort|add|pop> <file> [keys]

 sort: sort_keys sort <file>
      Exactly as it says on the tin: Sorts the keys alphabetically by game name.
      Creates and writes to the files [filename]_list[.ext] 
      and [filename]_sorted[.ext] (yes, it preserves your file extension!)
  add: sort_keys add <file> <keys>
      `keys` must be in the format `key name, key name, key name`, 
      i.e. `XXXXX-YYYYY-ZZZZZ xyz, 12345-67891-01112 123`.
      This will append the keys and name to the end of 
      your source file and then resort your keys - don't worry about duplicates,
      the sorting algorithm handles them for you.
  pop: sort_keys pop <file> <keys>
      `keys` can be any comma-delimited list of key and name (although not both!),
      i.e. `XXXXX-YYYYY-ZZZZZ, 123` would 'pop' (remove and print) the key-name pairs
      added in `add`s example. Note that this is a destructive command, 
      and that it should be used with care in order to avoid losing your keys!
```
