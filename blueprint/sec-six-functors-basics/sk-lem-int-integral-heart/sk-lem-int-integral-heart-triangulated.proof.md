+++
kind = "proof"
of = "det-lem-int-integral-heart-triangulated"
+++
(1) Derived completeness is stable under shifts and cones: $K$ is derived
complete if and only if
$R\varprojlim(\cdots\xrightarrow{\pi_E}K\xrightarrow{\pi_E}K)=0$, and this
derived limit is an exact functor of $K$. Reduction modulo $\pi_E$ is exact, so constructibility of the
reduction is stable under shifts and cones because bounded constructible
complexes on the étale site form a triangulated subcategory. Hence
$\Dbc(X,\mathcal O_E)$ is triangulated. Its objects are bounded: our schemes
are quasi-compact, and a derived complete complex whose reduction is bounded
is bounded (Stacks, Tag 09C2). Stability under truncation is
[det-lem-int-integral-heart-local-model](3).

(2) Let $\varphi:C\to C'$ be a morphism in $\Cons(X,\mathcal O_E)$ with cone
$D\in\Dbc(X,\mathcal O_E)$. Then $\ker\varphi=H^{-1}(D)$ and
$\operatorname{coker}\varphi=H^0(D)$, which lie in $\Dbc(X,\mathcal O_E)$ by
[det-lem-int-integral-heart-local-model](2) and are in degree $0$. So
$\Cons(X,\mathcal O_E)$ is an abelian subcategory. An extension
$0\to C'\to C\to C''\to0$ of modules gives a distinguished triangle
$C'\to C\to C''\to C'[1]$; if the ends are constructible, so is $C$ by (1).
Essential smallness: a constructible sheaf is determined up to isomorphism by
a finite stratification of $X$, finite presentations of
$\mathcal O_E$-modules giving local models on a pro-étale cover taken from a
fixed small site, and gluing morphisms; these data form a set.
