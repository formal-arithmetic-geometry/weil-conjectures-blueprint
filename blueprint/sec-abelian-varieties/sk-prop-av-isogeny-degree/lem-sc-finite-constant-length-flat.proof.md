+++
kind  = "proof"
of    = "lem-sc-finite-constant-length-flat"
+++
*Step 1: every fibre has length $r$.* The function
$y\mapsto\deg_y(f)$ is upper semicontinuous: $f_*\mathcal O_X$ is a
quasi-coherent $\mathcal O_Y$-module of finite type, so by Nakayama's
lemma (*reference: Stacks Project, Algebra, Lemma 10.20.1,
[Tag 00DV](https://stacks.math.columbia.edu/tag/00DV)*) lifts of a
$\kappa(y)$-basis of $f_*\mathcal O_X\otimes\kappa(y)$ generate
$f_*\mathcal O_X$ on an open neighbourhood $U$ of $y$, and then
$\deg_{y'}(f)\le\deg_y(f)$ for $y'\in U$. Let $y\in Y$ and let $U$ be
such a neighbourhood. As $Y$ is Jacobson, the nonempty locally closed
subset $U\cap\overline{\{y\}}$ contains a closed point $z$ of $Y$. Then
$r=\deg_z(f)\le\deg_y(f)$ because $z\in U$, and
$\deg_y(f)\le\deg_z(f)=r$ because $y$ lies in every open neighbourhood
of its specialization $z$. Hence $\deg_y(f)=r$.

*Step 2: local freeness.* The assertion is local on $Y$, so let
$Y=\operatorname{Spec}R$ with $R$ reduced and $X=\operatorname{Spec}S$;
as $f$ is finite and of finite presentation, $S$ is a finitely presented
$R$-module (a finite $R$-algebra of finite presentation is finitely
presented as a module). Let
$\mathfrak p\subset R$ be prime and choose $s_1,\dots,s_r\in S$ whose
images form a $\kappa(\mathfrak p)$-basis of $S\otimes\kappa(\mathfrak p)$.
By Nakayama's lemma $\varphi:R_{\mathfrak p}^{\oplus r}\to S_{\mathfrak p}$,
$e_i\mapsto s_i$, is surjective; let $K$ be its kernel. For every prime
$\mathfrak q\subseteq\mathfrak p$ the map
$\kappa(\mathfrak q)^{\oplus r}\to S\otimes\kappa(\mathfrak q)$ is a
surjection between $\kappa(\mathfrak q)$-vector spaces of the same
dimension $r$ (Step 1), hence injective; by right exactness of
$-\otimes\kappa(\mathfrak q)$ the image of $K$ in
$\kappa(\mathfrak q)^{\oplus r}$ is this kernel, so it is zero, i.e. the
coordinates of every element of $K$ lie in $\mathfrak qR_{\mathfrak p}$.
Hence they lie in $\bigcap_{\mathfrak q\subseteq\mathfrak p}\mathfrak qR_{\mathfrak p}$,
the nilradical of the reduced ring $R_{\mathfrak p}$, which is zero. So
$K=0$ and $S_{\mathfrak p}\cong R_{\mathfrak p}^{\oplus r}$. Since $S$ is
finitely presented, an isomorphism at $\mathfrak p$ spreads out to an
open neighbourhood of $\mathfrak p$: lift the isomorphism to a map
$R_g^{\oplus r}\to S_g$ for some $g\notin\mathfrak p$; its cokernel is
finitely generated and vanishes at $\mathfrak p$, so after inverting a
further element the map is surjective, and then its kernel is finitely
generated (as $S_g$ is finitely presented) and vanishes at $\mathfrak p$,
so it vanishes after inverting one more element.
Thus $f_*\mathcal O_X$ is locally free of rank $r$, and $f$ is flat.

*Step 3: the degree.* Let $X$ be integral with generic point $\eta$ and
put $y=f(\eta)$. Every point of $X_y$ is a specialization of $\eta$ with
the same image, so equals $\eta$, since a finite morphism has no
nontrivial specializations inside a fibre (incomparability for integral
ring maps). On an affine open $\operatorname{Spec}S\to\operatorname{Spec}R$
as above, with $S$ a domain and $y=\mathfrak q$, the ring
$S\otimes\kappa(\mathfrak q)=S_{\mathfrak q}/\mathfrak qS_{\mathfrak q}$
therefore has the single prime ideal $0$, so $\mathfrak qS_{\mathfrak q}=0$;
thus it is the domain $S_{\mathfrak q}$, finite-dimensional over
$\kappa(\mathfrak q)$, hence a field, namely $\kappa(\eta)$. So
$[\kappa(\eta):\kappa(y)]=\deg_y(f)=r$ by Step 1. If $f$ is a finite
surjective morphism of varieties, then $f(\eta)$ is the generic point of
$Y$, and $\kappa(\eta)=k(X)$, $\kappa(f(\eta))=k(Y)$, so
$\deg(f)=[k(X):k(Y)]=r$.
