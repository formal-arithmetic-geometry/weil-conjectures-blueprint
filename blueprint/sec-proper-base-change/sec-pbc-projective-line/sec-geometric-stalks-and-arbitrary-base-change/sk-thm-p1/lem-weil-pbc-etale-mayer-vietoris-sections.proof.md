+++
kind = "proof"
of = "lem-weil-pbc-etale-mayer-vietoris-sections"
uses = ["def-weil-pbc-etale-site"]
+++
The inclusions $U\to X$ and $V\to X$ are open immersions, hence etale, and their images $U$ and $V$ cover $X$; so they form a covering of $X$ in the small etale site [def-weil-pbc-etale-site]. The fibre product of the two open immersions is $U\cap V$ with its two inclusions, and $U\times_XU=U$, $V\times_XV=V$ because open immersions are monomorphisms.

The sheaf condition for this covering says that $F(X)\to F(U)\times F(V)\rightrightarrows F(U\times_XU)\times F(U\times_XV)\times F(V\times_XU)\times F(V\times_XV)$ is an equalizer. The components indexed by equal indices impose no condition, since $U\times_XU=U$ and the two restrictions to it agree; the components indexed by different indices compare the restrictions to $U\cap V$. Hence $s\mapsto(s|_U,s|_V)$ identifies $F(X)$ with the set of pairs $(s,t)\in F(U)\times F(V)$ with $s|_{U\cap V}=t|_{U\cap V}$.

This says exactly that $a$ is injective and that every pair with $b(s,t)=0$ is $a(r)$ for some $r\in F(X)$. Conversely $b\circ a=0$, since the restrictions of a global section to $U\cap V$ through $U$ and through $V$ agree by functoriality of restriction. So $0\to F(X)\xrightarrow{a}F(U)\oplus F(V)\xrightarrow{b}F(U\cap V)$ is exact.
