+++
kind = "proof"
of = "proposition-composition-base-change-rf-shriek--1"
order = 516003
uses = ["proposition-proper-base-change-degree-zero--1", "definition-injective-acyclicity--1", "proposition-proper-direct-image-constructible-complexes--6", "proposition-proper-direct-image-constructible-complexes--8", "lemma-inverse-image-tensor-product--1", "definition-compactification-refinement--2", "definition-compactification-refinement--3", "theorem-nagata-s-compactification-theorem--1"]
+++
*The composition isomorphism.* Choose compactifications $f=p\circ j$
and $g=q\circ j_Y$, with $j:X\to\overline X$ and $j_Y:Y\to\overline Y$ open and
$p,q$ proper. In the composite $Rq_*j_{Y!}Rp_*j_!$, the middle factor $j_{Y!}Rp_*$
applies a proper direct image before an extension by zero, and we
want to interchange the two.
Compactify the morphism $j_Y\circ p:\overline X\to\overline Y$ as
$\overline X\xrightarrow{j'}W\xrightarrow{r}\overline Y$, with $j'$ open,
$r$ proper and $\overline X$ dense in $W$. Then $r^{-1}(Y)=\overline X$,
because the open immersion $\overline X\to r^{-1}(Y)$ is a morphism from a proper
$Y$-scheme to a separated $Y$-scheme, hence proper, and its image is
closed, open and dense.

The interchange map is defined as follows. For $M$ in $D(\overline X_{\mathrm{pro}\acute{e}t},\Lambda)$, restriction to the open
$Y\subset\overline Y$ identifies $j_Y^*Rr_*j'_!M$ with $Rp_*M$, because
$r^{-1}(Y)=\overline X$, the restriction of $r$ over $Y$ is $p$, and
$j'_!M$ restricts to $M$ on $\overline X$. By the adjunction $j_{Y!}\dashv j_Y^*$, we obtain a map

$$
j_{Y!}Rp_*M\longrightarrow Rr_*j'_!M,
$$

which is the unique map restricting to the identity of $Rp_*M$ over $Y$.

For $M\in D^b_{\mathrm{ctf}}(\overline X,\Lambda)$, this map is an isomorphism. Over
$Y$ it is the identity, and over $\overline Y\setminus Y$ both sides vanish.
For the right-hand side, the vanishing follows from proper base change on $D^b_{\mathrm{ctf}}$
(Proposition [proposition-proper-base-change-localizing-categories]) for the inclusion
of $\overline Y\setminus Y$ into $\overline Y$, since $j'_!M$ vanishes on
$r^{-1}(\overline Y\setminus Y)=W\setminus\overline X$. Both sides preserve
direct sums on $\Loc(D^b_{\mathrm{ctf}}(\overline X,\Lambda))$
(Proposition [proposition-proper-direct-image-extension-zero]). Hence
Lemma [lemma-checking-isomorphisms-constructible-complexes] shows that
(5.9) is an isomorphism for all
$M\in\Loc(D^b_{\mathrm{ctf}}(\overline X,\Lambda))$. For $M=j_!K$ it gives

$$
Rq_*j_{Y!}Rp_*j_!K\simeq Rq_*Rr_*j'_!j_!K=R(qr)_*(j'j)_!K,
$$

and the right side is $R(gf)_!K$ computed with the compactification
$gf=(qr)\circ(j'j)$.

*Source:* the proof of Proposition [proposition-composition-base-change-rf-shriek].
