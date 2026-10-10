+++
kind  = "proof"
of    = "sk-prop-nagata-sketch-zmt"
+++
(i) Let $N_f$ be the normalization of $S$ in $X$, i.e. the relative
integral closure $\nu_f:N_f\to S$ with
$\nu_{f*}\mathcal O_{N_f}$ the integral closure of $\mathcal O_S$ in
$f_*\mathcal O_X$ (this is a quasi-coherent $\mathcal O_S$-algebra because
$f$ is quasi-compact and separated, hence quasi-compact and
quasi-separated). By construction $\nu_f$ is integral, in particular
affine, and $f$ factors as $f=\nu_f\circ\iota_f$ through the canonical
morphism $\iota_f:X\to N_f$. It remains to see that $\iota_f$ is an open
immersion. Both the formation of $N_f$ and the property of being an open
immersion are local on $S$ (the normalization commutes with restriction to
opens of $S$), so we may assume $S$ affine. Then $f$ is separated, of finite
type and quasi-finite at every point, and Zariski's Main Theorem in the
form 02LR, with the quasi-finite-locus input 03GW, says that the
canonical morphism $X\to N_f$ to the normalization of $S$ in $X$ is an open
immersion. Hence $f=\nu_f\circ\iota_f$ with $\iota_f$ an open immersion
and $\nu_f$ affine.

(ii) Put $R=\Gamma(X,\mathcal O_X)$, so that $X\to\operatorname{Spec}R$ is
a quasi-compact open immersion and the affine opens $X_f$, $f\in R$, form
a basis of $X$. By quasi-compactness choose $f_1,\dots,f_m\in R$ with
$X=\bigcup_jX_{f_j}$ and affine opens $V_j\subseteq S$ such that
$X_{f_j}\to S$ factors through $V_j$. Since $X\to S$ is locally of
finite type, each $\Gamma(X_{f_j},\mathcal O_X)=R_{f_j}$ is a finitely
generated $\mathcal O(V_j)$-algebra; clearing the denominators of finitely
many generators yields finitely many further elements $a_{jl}\in R$. The
global sections $f_j$, $a_{jl}$ define an $S$-morphism
$i:X\to\mathbb A^n_S$. Let $W_j\subseteq\mathbb A^n_S$ be the affine open
of points over $V_j$ at which the $j$-th coordinate is invertible; then
$i^{-1}(W_j)=X_{f_j}$, and $X_{f_j}\to W_j$ is a closed immersion, its
ring map being surjective (the image contains $\mathcal O(V_j)$, the
$a_{jl}$ and $f_j^{-1}$, which generate $R_{f_j}$). As the $W_j$ cover
$i(X)$, $i$ is an immersion. This is 04II. The argument uses
global sections of $X$ and is not local on $S$, which is why $X$ itself
has to be quasi-affine.
