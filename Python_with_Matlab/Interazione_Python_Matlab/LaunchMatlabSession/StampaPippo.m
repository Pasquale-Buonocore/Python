function a = StampaPippo(value)
    if value == 1
        disp("Python passed value 1");
        a = 1;
    elseif value == 2
        disp("Python passed value 2");
        a = 2;
    else
        disp("Python passed a not acceptable value. Return -1");
        a = -1;
    end
end