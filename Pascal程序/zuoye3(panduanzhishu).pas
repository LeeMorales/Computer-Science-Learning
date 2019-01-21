var
  n,s,i:integer;
begin
  s:=0;
  for i:=1 to n do
    begin;
      read(n);
      if n mod i=0 then s:=s+1;
    end;
  if s:=2,then writeln(zhishu)
          else writeln(heshu);
end.