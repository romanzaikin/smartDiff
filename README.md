# smartDiff

assume you have 2 text that change frequently, and you need to understand what exactly is changing, you can use my diff function in order to do that.

for example: you have text one:
```
text_one = """

Registers:
------------------------------------------------------------------------------------------------------------------------
r00=0x00000000	r01=0x00000000
r02=0x00000003	r03=0x00000000
r04=0x0000002f	r05=0x00000003
r06=0x00000075	r07=0x0000002d


Stack:
------------------------------------------------------------------------------------------------------------------------
00000000: 4D 02 16 2E 3A 0F                                 M...:.

Memory:
------------------------------------------------------------------------------------------------------------------------
00000000: CC CC CC CC CC CC CC CC  CC CC CC CC CC CC CC CC  ................
00000010: CC CC CC CC CC CC CC CC  CC CC CC CC CC CC CC CC  ................

Output:
------------------------------------------------------------------------------------------------------------------------
I'll do what you tell me"""
```

and the following data:
```
text_two = """

Registers:
------------------------------------------------------------------------------------------------------------------------
r00=0x00000000	r01=0x00000000
r02=0x00000003	r03=0x00000000
r04=0x00000071	r05=0x00000003
r06=0x00000076	r07=0x0000002d


Stack:
------------------------------------------------------------------------------------------------------------------------
00000000: 4D 02 16 2E 3A 0F 00                                 M...:.

Memory:
------------------------------------------------------------------------------------------------------------------------
00000000: CC CC CC CC CC CC CC CC  CC CC CC CC CC CC CC CC  ................
00000010: CC CC CC CC CC CC CC CC  CC CC CC CC CC CC CC CC  ................

Output:
------------------------------------------------------------------------------------------------------------------------
I'll do what you tell!"""
```
you can use the following function to diff between them:

```
diff(text_one, text_two, "red", ['reverse', 'bold'])
```

the output will look like this:

![alt tag](https://raw.githubusercontent.com/romanzaikin/smartDiff/master/image.PNG)
Have fun!