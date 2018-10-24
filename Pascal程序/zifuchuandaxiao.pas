var
  s1,s2:string;
begin
  readln(s1);
  readln(s2);
  if s1>s2 then
  begin
    write(s1);write(s2);
  end
  else begin
         write(s2);write(s1);
       end;
end.