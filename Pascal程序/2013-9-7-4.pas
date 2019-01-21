var
  i:longint;
begin
  for i:=2000 downto 1 do
  if i mod 30=0 then
                  begin
                    write(i);
                    break;
                  end;
end.

