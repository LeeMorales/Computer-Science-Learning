var
  a,i,j,b,c,k,n:integer;
begin
  for i:=1 to 4 do
  begin
    for k:=1 to 4-i do
    write(' ');
    for j:=(i+64) downto 65 do
    write(chr(j));
    for b:=66 to (i+64) do
    write(chr(b));
    writeln;
  end;
  for i:=3 downto 1 do
  begin
    for k:=4-i downto 1 do
    write(' ');
    for j:=(i+64) downto 65 do
    write(chr(j));
    for b:=66 to (i+64) do
    write(chr(b));
    writeln;
  end;
end.
