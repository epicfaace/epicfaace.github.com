SyntaxHighlighter.defaults['gutter'] = true;
SyntaxHighlighter.defaults['toolbar'] = false;
SyntaxHighlighter.all();
$(window).bind("load", function() {
   $(".gutter .line").attr("unselectable","on");
});