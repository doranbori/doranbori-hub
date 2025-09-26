import { ReactNode } from "react";

export default function Card({
  title,
  children,
}: {
  title: string;
  children: ReactNode;
}) {
  return (
    <div className="mb-4 overflow-hidden rounded-2xl shadow-md bg-[color:var(--espresso-dark)]">
      {/* 제목 영역: 단순 그라디언트 포인트 */}
      <div
        className="relative py-4 px-6 font-bold text-xl"
      >
        {title}
        <div
          className="absolute bottom-0 left-0 w-full h-1 rounded-full
                     bg-gradient-to-r from-[color:var(--rustynut-light)] to-[color:var(--rustynut-dark)]"
        />
      </div>

      {/* 내용 영역 */}
      <div
        className="no-margin-p bg-[color:var(--chestnut-dark)] py-4 px-6 leading-relaxed"
      >
        {children}
      </div>
    </div>
  );
}
