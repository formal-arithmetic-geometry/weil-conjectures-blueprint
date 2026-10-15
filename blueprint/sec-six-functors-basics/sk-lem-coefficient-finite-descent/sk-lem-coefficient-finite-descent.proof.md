+++
kind  = "proof"
of    = "sk-lem-coefficient-finite-descent"
+++
To descend a lisse $\QbarX$-module we work with its transition matrices on a pro-étale cover.
Two facts describe the entries of such matrices on a quasi-compact object $V$ of
$X_{\mathrm{proét}}$.

- Sections of a filtered colimit of sheaves over $V$ are the filtered colimit of the
  sections. Indeed, every covering of $V$ has a finite refinement by quasi-compact objects,
  and the sheaf condition for a finite covering is a finite limit, which commutes with
  filtered colimits (this is the degree-zero case of \stacks{0739}). Since
  $\QbarX=\varinjlim_EE_X$ ([sk-prop-sfb-qlbar-colimit-x]), finitely many sections of
  $\QbarX$ over $V$ all lie in $E_X(V)$ for one finite $E/\mathbf Q_\ell$.
- $E_X(V)$ is the ring of continuous functions $|V|\to E$. A continuous function on a
  quasi-compact space has compact image, which lies in $\ell^{-m}\cO_E$ for some $m$, so this
  follows from the description of $\cO_{E,X}$ in [sk-prop-sfb-qlbar-colimit-x].

Affine, hence quasi-compact, pro-étale coverings and quasi-compact refinements exist by
\stacks{0988}. Details: [det-lem-coefficient-finite-descent-sections].

(1) Let $L$ be a lisse $\QbarX$-module. Since $X$ is quasi-compact, $L$ is free on a finite
covering of $X$ by quasi-compact (we may take affine) pro-étale objects $V_k$. Since $X$ is
quasi-separated, the intersections $V_k\times_XV_{k'}$ are quasi-compact. On them, $L$ is
described by finitely many transition matrices with entries in $\QbarX$, and so are their
inverses. By the two facts above, all these entries lie in $E_X$ for one finite $E$. The
cocycle identities hold over $E_X$ because $E_X\to\QbarX$ is injective. Descent of sheaves
along the covering then produces a lisse $E_X$-module $L_E$ with $(L_E)_{\Qlb}\cong L$. The
same argument descends morphisms between lisse sheaves. Details:
[det-lem-coefficient-finite-descent-lisse].

(2) Extension of scalars $F_X\otimes_{E_X}-$ is left adjoint to restriction of scalars
$D(X_{\mathrm{proét}},F)\to D(X_{\mathrm{proét}},E)$, so
$\Hom_{D(X_{\mathrm{proét}},F)}(C_F,D_F[r])=\Hom_{D(X_{\mathrm{proét}},E)}(C,D_F[r])$, and similarly
for $\Qlb$. Represent $D$ by a bounded complex $D^\bullet$. The complexes
$D^\bullet\otimes_{E_X}F_X$ form a filtered system of complexes of $E_X$-modules, all vanishing
below the lower bound of $D^\bullet$, and their colimit is $D^\bullet\otimes_{E_X}\QbarX$, which
represents $D_{\Qlb}$. [sk-lem-constructible-ext-continuity], applied to $C\in\Dbc(X,E)$,
gives
$$
\varinjlim_F\Hom_{D(X_{\mathrm{proét}},E)}(C,D_F[r])\xrightarrow{\ \sim\ }\Hom_{D(X_{\mathrm{proét}},E)}(C,D_{\Qlb}[r]),
$$
which is the claim after the adjunction. Details: [det-lem-coefficient-finite-descent-hom].

(3) First let $K$ be a constructible $\QbarX$-module, with filtration
$F_1\subset\cdots\subset F_m=K$ as in [sk-lem-coefficient-heart] (3). We descend $F_k$ by
induction on $k$. The subquotient $F_k/F_{k-1}=a_!L$ descends because $L$ does, by (1), and
$a_!$ commutes with extension of scalars, as functors
$\Mod(S_{\mathrm{proét}},E)\to\Mod(X_{\mathrm{proét}},\Qlb)$. Suppose $F_{k-1}$ and $F_k/F_{k-1}$
descend to $E$. The extension $0\to F_{k-1}\to F_k\to F_k/F_{k-1}\to0$ is a distinguished
triangle, classified by a morphism $F_k/F_{k-1}\to F_{k-1}[1]$. By (2) this morphism descends
to some finite $F\supset E$, and its cone over $F$ is a model of $F_k$.

For a bounded complex $K$, induct in the same way along the truncation triangles
$\tau_{<q}K\to K\to\mathcal H^q(K)[-q]\to$. Once $\tau_{<q}K$ and $\mathcal H^q(K)$ have models
over a finite $E$, the connecting morphism $\mathcal H^q(K)[-q-1]\to\tau_{<q}K$ descends after a
finite extension by (2), and the cone of the descended morphism is a model of $K$. Each step
enlarges $E$ finitely often, so after finitely many steps $K$ is defined over one finite $E$.
Details: [det-lem-coefficient-finite-descent-objects].
