+++
id = "det-sp-tower-gluing"
kind = "lemma"
title = "Gluing the local tower adjunctions"
order = 3021
uses = ["det-sp-tower-p1-adjunction", "det-sp-tower-shriek-levels", "det-sp-tower-bound-uniform", "det-sp-reduction-exceptional"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$. For each
$K_\bullet\in\Dctf(Y_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$ there is a pair
$(f^!_\bullet K_\bullet,\varepsilon_\bullet(K_\bullet))$ with
$f^!_\bullet K_\bullet\in\Dctf(X_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$ and
$\varepsilon_\bullet(K_\bullet):Rf_{!,\bullet}f^!_\bullet K_\bullet\to K_\bullet$ representing
$M_\bullet\mapsto\operatorname{Hom}(Rf_{!,\bullet}M_\bullet,K_\bullet)$ on
$\Dctf(X_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$, such that:

1. on each coordinate chart $f|_U=p_d\circ e$ ($e:U\to\mathbf A^d_Y$ étale),
   $f^!_\bullet K_\bullet|_U\simeq e_\bullet^*p_{d,\bullet}^*K_\bullet(d)[2d]$ with counit
   the iterated projective-line integration followed by the fibre sum of $e$;
2. the pair is unique up to unique isomorphism, hence $K_\bullet\mapsto f^!_\bullet K_\bullet$
   is a functor right adjoint to $Rf_{!,\bullet}$;
3. $(f^!_\bullet K_\bullet)_n\simeq f^!_{\mathcal O_E/\ell^n}K_n$ compatibly with
   counits and units, and the reduction maps of $f^!_\bullet K_\bullet$ are the
   composites of the coefficient comparisons $c_{n,m}$ of
   [det-sp-reduction-exceptional] with $f^!$ of the reduction maps of $K_\bullet$.
