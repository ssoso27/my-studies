/*
중급 057) foreach와 Lambda 형식을 이용하여 List 출력하기
- 학습 내용 : List에 저장된 데이터를 foreach와 Lambda 형식을 이용하여 List를 출력해 보자.
- 힌트 내용 : 향상된 for와 비슷한 형태로, 인덱스 없이 순서대로 출력하는 방법을 이용한다.
 */

import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;

public class Q057 {
    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(1, 6, 16, 22, 23, 33);
        list.forEach(m -> System.out.print(m + ", "));
        System.out.println();

        Consumer<Integer> consume = (Integer m) -> System.out.print(m + ", ");
        list.forEach(consume);
    }
}
