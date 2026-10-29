+++
kind = "proof"
of = "sk-thm-sfb-qlbar-two-colimit"
uses = ["sk-lem-constructible-ext-continuity", "sk-lem-coefficient-heart", "sk-lem-lisse-finite-descent"]
+++
Morphisms descend because $\QbarX$ is the filtered colimit of the $E'_X$ and Hom out of a
constructible complex commutes with this colimit ([sk-lem-constructible-ext-continuity]).
Objects are built from lisse sheaves by finitely many extensions, each classified by a
morphism, and so they descend as well.

(1) Extension of scalars $E'_X\otimes_{E_X}-$ is left adjoint to restriction of scalars
$D(X_{\mathrm{proét}},E')\to D(X_{\mathrm{proét}},E)$. Hence
$\Hom_{D(X_{\mathrm{proét}},E')}(C_{E'},D_{E'}[r])=\Hom_{D(X_{\mathrm{proét}},E)}(C,D_{E'}[r])$, and
similarly for $\Qlb$. Represent $D$ by a bounded complex $D^\bullet$. The complexes
$D^\bullet\otimes_{E_X}E'_X$ form a filtered system of complexes of $E_X$-modules, all vanishing
below the lower bound of $D^\bullet$, and their colimit is $D^\bullet\otimes_{E_X}\QbarX$, which
represents $D_{\Qlb}$. Applying [sk-lem-constructible-ext-continuity] to $C\in\Dbc(X,E)$, we get
$$
\varinjlim_{E'}\Hom_{D(X_{\mathrm{proét}},E)}(C,D_{E'}[r])\xrightarrow{\ \sim\ }\Hom_{D(X_{\mathrm{proét}},E)}(C,D_{\Qlb}[r]),
$$
which is the claim after the adjunction. Details: [det-lem-coefficient-finite-descent-hom].

(2) First let $K$ be a constructible $\QbarX$-module, with filtration
$N_1\subset\cdots\subset N_m=K$ as in [sk-lem-coefficient-heart] (3). We descend $N_k$ by
induction on $k$. The subquotient $N_k/N_{k-1}=a_!L$ descends because $L$ does, by
[sk-lem-lisse-finite-descent], and $a_!$ commutes with extension of scalars. Suppose $N_{k-1}$
and $N_k/N_{k-1}$ descend to $E$. The extension $0\to N_{k-1}\to N_k\to N_k/N_{k-1}\to0$ gives a
distinguished triangle, which is classified by a morphism $N_k/N_{k-1}\to N_{k-1}[1]$. By (1)
this morphism descends after a finite extension of $E$, and the fibre of the descended
morphism, that is, its cone shifted by $[-1]$, is a model of $N_k$.

For a bounded complex $K$, we argue in the same way by induction on the number of nonzero
cohomology sheaves. Let $i$ be the largest degree with $\mathcal H^i(K)\neq0$, and consider the
truncation triangle $\tau_{<i}K\to K\to\mathcal H^i(K)[-i]\to$. Once $\tau_{<i}K$ and
$\mathcal H^i(K)$ have models over a finite $E$, the connecting morphism
$\mathcal H^i(K)[-i-1]\to\tau_{<i}K$ descends after a finite extension by (1), and the cone of
the descended morphism is a model of $K$. Each step replaces $E$ by a finite extension, so
that after finitely many steps $K$ is defined over a single finite $E$. Details:
[det-lem-coefficient-finite-descent-objects].
