+++
kind = "proof"
of = "sk-thm-tf-sp-zero-section"
uses = ["sk-lem-tf-sp-defect-exchanges", "sk-lem-tf-sp-generic-divisor", "sk-lem-tf-sp-constant-family", "sk-thm-pe-constructible-comparison", "sk-cor-pe-finite-tor-comparison"]
+++
Let $C_{X,Z}(L)$ be the cofibre of $\epsilon_{X,Z}(L)$, as in [sk-lem-tf-sp-defect-exchanges]. The
main step is the vanishing $C_{X,Z}(L)=0$ for every $L\in D^b_c(X_{\mathrm{\acute et}},A)$; the last
paragraph transports it to $\Dctf$. The vanishing is proved for all bounded constructible complexes
because the cokernels $j_!G'$ in the dimension shifting of [sk-lem-tf-sp-generic-divisor] may have
infinite Tor dimension.

By [sk-lem-tf-sp-defect-exchanges], replace $L$ by $j_!j^*L$, so that $i^*L=0$. Let
$b:X'=\operatorname{Bl}_ZX\to X$. The unit $L\to Rb_*b^*L$ is an isomorphism: it is so away from
$Z$ because $b$ is an isomorphism there, and on $Z$ proper base change identifies its target with
the cohomology of a fibre with zero coefficients. Proper exchange then gives
$C_{X,Z}(L)\simeq C_{X,Z}(Rb_*b^*L)\simeq Rb_{Z*}C_{X',b^{-1}Z}(b^*L)$, which reduces the
assertion to the inverse-image pair $(X',b^{-1}Z)$. The pullback ideal is invertible on the
blow-up (empty components cause no problem), so we have reduced to a Cartier divisor.

The assertion is local. Take $X$ affine with $Z=V(h)$ for a function $h$. Choose algebra
generators for $\mathcal O(X)$ and append $h$ as the last coordinate. This gives a closed immersion

$$
a:X\hookrightarrow\mathbf A^n,\qquad Z=a^{-1}(\mathbf A^{n-1}\times\{0\})
$$

schematically. Proper exchange and the faithfulness of the closed direct image reduce the
assertion to $(\mathbf A^n,\mathbf A^{n-1}\times\{0\})$.

Induct on $n\geq1$. We may again assume $L|_Z=0$. [sk-lem-tf-sp-generic-divisor] shows that the
closure $Y$ of the support of $C_{X,Z}(L)$ is a proper closed subset of the hyperplane $Z$. For
$n=1$ it is empty and the assertion follows. For $n>1$, choose a line $\lambda$ in the vector space
$Z$ such that the linear projection

$$
q:X\longrightarrow X'=X/\lambda\simeq\mathbf A^{n-1}
$$

is finite on $Y$. To see existence, choose the projective point $\mathbf P(\lambda)$ outside the
part at infinity of the projective closure of $Y$ in $\mathbf P(Z\oplus k)$. The projection is then
finite on $Y$ by the usual proof of linear Noether normalization. Set $Z'=Z/\lambda$, a coordinate
hyperplane in $X'$, and compactify the $\lambda$-direction:

$$
\bar q:\bar X=\mathbf P^1\times X'\longrightarrow X',\qquad
\bar Z=\bar q^{-1}(Z'),\qquad
v:X\hookrightarrow\bar X,\qquad \bar L=v_!L.
$$

Let $\bar q_Z\colon\bar Z\to Z'$ be the restriction of $\bar q$. Proper exchange and the induction
hypothesis yield

$$
R\bar q_{Z*}C_{\bar X,\bar Z}(\bar L)\simeq C_{X',Z'}(R\bar q_*\bar L)=0.
$$

By locality, $C_{\bar X,\bar Z}(\bar L)$ is supported on $Y\cup(\bar Z\setminus Z)$. This is a
closed subset finite over $Z'$: $Y$ is finite and therefore remains closed in $\bar Z$, and
$\bar Z\setminus Z$ is the infinity section of $\bar Z\to Z'$. As in
[sk-lem-tf-sp-constant-family], finite direct image is conservative on complexes with this support.
Thus $C_{\bar X,\bar Z}(\bar L)=0$, and restriction gives $C_{X,Z}(L)=0$, which proves the
vanishing on the étale site.

Finally, by the finite-coefficient comparison ([sk-thm-pe-constructible-comparison],
[sk-cor-pe-finite-tor-comparison]) $K$ and its maps descend to the classical étale constructible
category, where the vanishing of $C_{X,Z}$ has just been proved. The comparison is exact and fully
faithful, and it identifies pullback, proper direct image and their adjunction units. It therefore
carries the étale map (1) to the map in the statement, which is an isomorphism.
