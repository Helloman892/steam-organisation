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
      `keys` can be any comma-delimited list of keys and names (although not both!),
      i.e. `XXXXX-YYYYY-ZZZZZ, 123` would 'pop' (remove and print) the key-name pairs
      added in `add`s example. Note that this is a destructive command,
      and that it should be used with care in order to avoid losing your keys!
```

##### Example files (note: if any of these work, it's sheer luck):
###### spares
```
1FHRY-PJAWN-KHCJS | Teslagrad
E0H61-U5738-ASSHF | BlazBlue: Chronophantasma Extend
TD7IJ-P5BUZ-BJFI4 | Sanctum 2
IWG1Y-229Z3-3SP18 | Deep Dungeons of Doom
EIO1Q-11OFN-PEEH3 | Gunpoint
HVF6V-JXADO-38WTX | Chivalry: Medieval Warfare
GFZSK-FBSK7-625AH | Teslagrad
```
###### spares_list
```
BlazBlue: Chronophantasma Extend
Chivalry: Medieval Warfare
Deep Dungeons of Doom
Gunpoint
Sanctum 2
Teslagrad * 2

Total keys: 7
```
###### spares_sorted
```
E0H61-U5738-ASSHF | BlazBlue: Chronophantasma Extend
HVF6V-JXADO-38WTX | Chivalry: Medieval Warfare
IWG1Y-229Z3-3SP18 | Deep Dungeons of Doom
EIO1Q-11OFN-PEEH3 | Gunpoint
TD7IJ-P5BUZ-BJFI4 | Sanctum 2
1FHRY-PJAWN-KHCJS | Teslagrad
GFZSK-FBSK7-625AH | Teslagrad
```

##### Troubleshooting
There, uh, shouldn't be any problems. If you run into any exceptions that I haven't caught, let me know - my testing wasn't exactly *rigorous*.
