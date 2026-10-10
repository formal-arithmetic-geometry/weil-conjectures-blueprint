+++
kind  = "proof"
of    = "pqf-lem-locnoeth-lft"
+++
Let $x\in X$ and put $s=f(x)$. Since $S$ is locally Noetherian
([pqf-def-locnoeth]) there
is an affine open neighbourhood $V=\operatorname{Spec}R$ of $s$ with
$R$ Noetherian, and since $f$ is locally of finite type there is an
affine open neighbourhood $U=\operatorname{Spec}A$ of $x$ with
$f(U)\subset V$ and such that $A$ is a finite type $R$-algebra,
i.e. $A=R[y_1,\dots,y_n]/I$ for some ideal $I$ (the ring-level
existence of such a pair $(U,V)$ is the content of the local finite
type condition in [def-weil-pbc-scheme-conventions]; shrinking
$U$ around $x$ preserves it). By the Hilbert basis theorem, $R$
Noetherian implies the polynomial ring $R[y_1,\dots,y_n]$ Noetherian,
hence its quotient $A$ is Noetherian; the localization $A_{\mathfrak p}$ at the prime $\mathfrak p$ of $x$ is Noetherian (ideals of
$S^{-1}A$ are extended ideals: $\mathfrak b\mapsto S^{-1}\mathfrak b$ is a bijection onto the ideals of $S^{-1}A$, so a
chain of ideals in $S^{-1}A$ lifts to a finite chain in $A$). Hence
$\mathcal O_{X,x}$ is Noetherian for every $x$, i.e. $X$ is locally
Noetherian.
