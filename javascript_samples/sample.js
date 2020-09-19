/* eslint-env jquery */

$(document).ready(function () {
  // Event handlers
  $("#btn1").click(function () {
    test01();
  });
  $("#btn2").click(function () {
    test02();
  });
  $("#btn3").click(function () {
    clearTextArea();
  });
});

function clearTextArea() {
  $("#text1").val("");
}

function test01() {
  $("#text1").val("You pressed Button1");
}

function test02() {
  $("#text1").val("You pressed Button2");
}
