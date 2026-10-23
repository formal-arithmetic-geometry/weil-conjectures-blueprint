+++
id = "det-sp-tower-gamma"
kind = "proposition"
title = "Tower orientation and tower purity isomorphism"
order = 3022
uses = ["det-sp-tower-gluing", "det-sp-reduction-compatibilities", "det-sp-reduction-direct-image", "thm-pur-diagonal-dualizing-object"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$ and put
$\omega_{f,\bullet}=f^!_\bullet(\mathcal O_{E,Y}/\ell^\bullet)$.

1. The diagonal construction gives an orientation
   $(\mathcal O_{E,X}/\ell^\bullet)(d)[2d]\xrightarrow{\sim}\omega_{f,\bullet}$ in
   $D(\operatorname{Tow}(X,\mathcal O_E))$ whose level $n$ is the finite orientation with
   coefficients $\mathcal O_E/\ell^n$.
2. Its inverse composed with the tensor map (built from the tower counit and the
   projection formula) is an isomorphism in
   $\Dctf(X_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$, natural in
   $K_\bullet\in\Dctf(Y_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$,
   $$
   \gamma_{f,\bullet}(K_\bullet):f_\bullet^*K_\bullet(d)[2d]\xrightarrow{\ \sim\ }f_\bullet^!K_\bullet,
   $$
   with level $n$ equal to $\gamma_{f,\mathcal O_E/\ell^n}(K_n)$.
3. Both $Rf_{!,\bullet}$ and $f^!_\bullet$ preserve normalized towers.
