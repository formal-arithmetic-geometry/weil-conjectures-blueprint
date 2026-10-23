+++
kind  = "proof"
of    = "lem-wf-arith-extension-group"
+++
By [lem-wf-conjugation-geometric-monodromy], $\alpha$ is an
automorphism of the group $H_{\mathrm{geom}}$ of
[def-wf-geometric-monodromy-group], so each power $\alpha^m$ is a
group automorphism and $\alpha^{m+n}=\alpha^m\circ\alpha^n$. The
displayed product is therefore associative:

$$
(h,m)\bigl((h',n)(h'',p)\bigr)
=(h\alpha^m(h')\alpha^{m+n}(h''),m+n+p)
=\bigl((h,m)(h',n)\bigr)(h'',p).
$$

The element $(1,0)$ is a two-sided identity because
$\alpha^m(1)=1$, and the displayed formula for $(h,m)^{-1}$ is a
two-sided inverse because $\alpha^{-m}(\alpha^m(h'))=h'$. Finally
$\deg_G\bigl((h,m)(h',n)\bigr)=m+n =\deg_G(h,m)+\deg_G(h',n)$, so $\deg_G$ is a homomorphism; it is
surjective since $\deg_G(1,m)=m$, and its kernel is the set of pairs
$(h,0)$, namely $H_{\mathrm{geom}}\times\{0\}$, as in
[def-wf-arithmetic-monodromy-extension].
