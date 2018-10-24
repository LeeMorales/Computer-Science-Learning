var
  n,m,i,s,l,z:longint;
begin
  write(l,z);
  readln(m,n);
  i:=1;
  s:=m*i;
  while s mod n<>0 do
    begin
      i:=i+1;
      s:=m*i;
    end;
    writeln('m&n zuixiaogongbeishu',s);
end.