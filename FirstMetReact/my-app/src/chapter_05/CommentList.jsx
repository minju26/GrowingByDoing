import React from "react";
import Comment from "./Comment";

const comments = [
    {
        name: "김민주",
        comment: "안녕하세요, 김민주입니다.",
    },
    {
        name: "이지언",
        comment: "안녕하세요, 똑독한 이지언입니다.",
    },
    {
        name: "문가영",
        comment: "안녕하세요, 예쁜 문가영입니다.",
    },
];

function CommentList(props) {
    return (
        <div>
            {comments.map((comment) => {
                return (
                    <Comment name={comment.name} comment={comment.comment} />
                );
            })}
        </div>
    );
}

export default CommentList;