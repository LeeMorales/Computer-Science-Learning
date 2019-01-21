 var
  a:array[1..121370] of real;
  i,k,s:longint;
begin
  a[1]:=1;
  a[2]:=1;
  for i:=3 to 100 do
   a[i]:=a[i-1]+a[i-2];
   for i:=1 to 121370 do
   for k:=1 to 121370 do
    write(a[i],' ',i);
end.
