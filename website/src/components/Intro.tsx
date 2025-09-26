export default function Intro({
  title="Introduction",
  children,
}: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <div className="no-margin-p relative p-6 rounded-2xl bg-[color:var(--espresso-dark)] shadow-md overflow-hidden">
      {/* 상단 라인: rustynut 계열 그라디언트 */}
      <div
        className="absolute inset-x-0 top-0 h-1 rounded-t-2xl 
        bg-gradient-to-r from-[color:var(--rustynut-light)] via-[color:var(--rustynut)] to-[color:var(--rustynut-darkest)]"
      />

      <div className="space-y-3">
        {title && (
          <h2 className="text-xl font-semibold text-[color:var(--grey-100)]">
            {title}
          </h2>
        )}
        <p className="text-base leading-relaxed">
          {children}
        </p>
      </div>
    </div>
  );
}
