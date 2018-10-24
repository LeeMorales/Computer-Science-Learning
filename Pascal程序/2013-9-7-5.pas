var
  i:longint;
begin
  i:=2000;
  while i>=1 do
  if i mod 30=0 then
                  begin
                    write(i);
                    break;
                 end
                 else i:=i-1;
end.
