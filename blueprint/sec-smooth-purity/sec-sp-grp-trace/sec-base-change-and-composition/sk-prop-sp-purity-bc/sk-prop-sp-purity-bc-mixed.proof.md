+++
kind = "proof"
of = "det-sp-mixed-base-change"
+++
*Direct images.* Choose a compactification $f=\bar f\circ j$ and pull it back to
$Y'$, giving $f'=\bar f'\circ j'$. Both $b$ and $\beta$ are composites of the
corresponding maps for $j$ and for $\bar f$, so it suffices to treat these
separately. For the open immersion $j$ both sides are the evident
identification of extensions by zero ($j_!$ commutes with pullback and with
extension of scalars on the nose). For the proper map $\bar f$, both $b^{\bar f}$
and proper base change are transposes of the counit of $L\bar f^*\dashv R\bar f_*$
on the derived categories of $A$-module sheaves on the pro-étale sites, after
extension of scalars and after pullback respectively. Both sides of the first
identity are maps $v_B^*((R\bar f_*N)_B)\to R\bar f'_*(u_B^*(N_B))$; transposing
under $L\bar f'^*\dashv R\bar f'_*$, each becomes the pulled-back counit
$u^*\bar f^*R\bar f_*N\to u^*N$ with scalars extended, by naturality of the counits
and the compatibility of transposition with pullback and with extension of
scalars. Hence the two sides agree.

*Exceptional images.* Both sides of the second identity are maps
$(u_A^*f_A^!K)_B\to(f')_B^!v_B^*K_B$. Transpose under
$R(f')_{!,B}\dashv(f')_B^!$, i.e. compose $R(f')_{!,B}$ of each side with
$\varepsilon_{f',B}(v_B^*K_B)$. Since $c^{f'}$ is defined by transposing the
counit composed with $b^{f'}$, and $e_{f,A}$ by transposing the pulled-back
counit composed with $\beta_{f,A}^{-1}$, the transpose of the left side is
$(v_A^*\varepsilon_{f,A}(K))_B$ composed with the inverses of
$b^{f'}(u_A^*f_A^!K)$ and $(\beta_{f,A}(f^!_AK))_B$; the transpose of the right
side is $v_B^*(\varepsilon_{f,B}(K_B))\circ v_B^*Rf_{!,B}(c^f_{A,B}(K))$ composed with
the inverse of $\beta_{f,B}((f_A^!K)_B)$, which by the defining identity of $c^f$
equals $v_B^*((\varepsilon_{f,A}(K))_B\circ b^f(f^!_AK)^{-1})\circ\beta_{f,B}^{-1}$.
The first identity, applied to $M=f^!_AK$, says exactly that these two inverse
composites agree. Hence the transposes agree and so do the maps.
