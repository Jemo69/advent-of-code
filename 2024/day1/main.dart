import 'dart:io';
void main() {
try {

  var input = File('input.txt').readAsLinesSync();
    var list1 = [];
    var list2 = [];
    input.forEach((line) {
        var x = line.split('\n');
        print(x);

        for (var i = 0; i < x.length; i++) {
            list1.add(x[i]);
        print(list1);
        print(list2);
        }
    });
}
    catch (e) {
    print(e);
    }
}
