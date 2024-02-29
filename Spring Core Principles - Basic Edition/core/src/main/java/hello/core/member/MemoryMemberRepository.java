package hello.core.member;

import java.util.HashMap;
import java.util.Map;

public class MemoryMemberRepository implements MemberRepository{


    private static Map<Long, Member> store = new HashMap<>();
    //실무에서는 동시성 이슈로 인해 ConcurrentHashMap을 주로 사용:  ConcurrentHashMap은 읽기는 여러 쓰레드가 동시에 가능, 쓰기는 특정 세그먼트 or 버킷에 대한 Lock을 사용

    @Override
    public void save(Member member) {
        store.put(member.getId(), member);
    }

    @Override
    public Member findById(Long memberId) {
        return store.get(memberId);
    }
}
