+++
kind = "proof"
of = "lem-weil-pbc-henselian-of-nil-maximal-ideal"
uses = ["def-weil-pbc-henselian-terminology", "lem-weil-pbc-henselian-local-root-lifting"]
+++
Let $f\in R[T]$ and $x\in R$ with $f(x)\in\mathfrak m$ and $f'(x)$ a unit. Then $f(x)$ is nilpotent, and Newton iteration $x_{k+1}=x_k-f(x_k)/f'(x_k)$ terminates: the error is squared at each step, and nilpotent corrections keep $f'(x_k)$ a unit, so if $f(x)^N=0$ then after $k$ steps with $2^k\ge N$ the error vanishes. This gives $a\in R$ with $f(a)=0$ and $a-x$ nilpotent, hence $a-x\in\mathfrak m$. Thus simple roots of monic polynomials modulo $\mathfrak m$ lift, which is equivalent to henselianity in the sense of [def-weil-pbc-henselian-terminology] by [lem-weil-pbc-henselian-local-root-lifting]. If $R$ has Krull dimension $0$, then $\mathfrak m$ is the only prime ideal, so it equals the nilradical, and the first part applies.
