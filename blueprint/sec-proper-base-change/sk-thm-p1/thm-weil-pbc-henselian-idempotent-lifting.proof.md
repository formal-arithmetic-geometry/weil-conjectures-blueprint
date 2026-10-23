+++
kind  = "proof"
of    = "thm-weil-pbc-henselian-idempotent-lifting"
uses = ["lemma-weil-pbc-stein-connectedness", "def-weil-pbc-scheme-conventions"]
+++
The closed fibre $i:Z_0\to Z$ is a closed immersion whose image is
$p^{-1}(V(I))$, where $p:Z\to\operatorname{Spec}A$ is the structure map. By
[lemma-weil-pbc-stein-connectedness], $Z$ is spectral and every irreducible
closed subset of $Z$ meets $Z_0$ in a nonempty connected subset. In particular
every nonempty closed subset $C\subseteq Z$ meets $Z_0$: it contains the
closure of one of its points, which is irreducible.

*Open and closed subsets.* Let $U,V\subseteq Z$ be open and closed with
$U\cap Z_0=V\cap Z_0$. Then $U\setminus V$ is closed and does not meet $Z_0$,
so it is empty; likewise $V\setminus U$, hence $U=V$. Conversely let
$Z_0=V_1\sqcup V_2$ be a decomposition into open and closed subsets; each
$V_k$ is closed in $Z$, hence quasi-compact. Put
$W_k=\{x\in Z:\overline{\{x\}}\cap V_k\neq\emptyset\}$, the set of
generizations of $V_k$. Every $\overline{\{x\}}\cap Z_0$ is nonempty and
connected, so it lies in exactly one of $V_1,V_2$; hence $Z=W_1\sqcup W_2$ and
$W_k\cap Z_0=V_k$. Each $W_k$ is closed. Since $Z$ is spectral and $V_k$ is
quasi-compact, $W_k$ is the intersection of the quasi-compact opens containing
$V_k$, so it is pro-constructible, and every point $x$ of its closure is a
specialization of some $x'\in W_k$. A point $z\in\overline{\{x\}}\cap Z_0$
then lies in $\overline{\{x'\}}\cap Z_0\subseteq V_k$, so $x\in W_k$. Hence
$W_1$ is open and closed in $Z$ with closed fibre $V_1$. Thus $U\mapsto U\cap Z_0$ is a bijection from
the open and closed subsets of $Z$ to those of $Z_0$.

*Idempotents.* On any scheme $X$, an idempotent $e\in H^0(X,\mathcal O_X)$
determines the open and closed subset of points where its germ is $1$, and this
is a bijection between idempotents of $H^0(X,\mathcal O_X)$ and open and
closed subsets of $X$ [def-weil-pbc-scheme-conventions]; it is compatible with
pullback along morphisms of schemes. Applied to $Z$ and $Z_0$ and the
restriction along $i$, the bijection on open and closed subsets becomes the
bijection on idempotents.

The restriction map $H^0(Z,\mathcal O_Z)\to H^0(Z_0,\mathcal O_{Z_0})$ itself
is not an isomorphism. For $A=k[[t]]$, $I=(t)$ and $Z=\mathbf P^1_A$ it is
$k[[t]]\to k$. So only idempotents are compared.
