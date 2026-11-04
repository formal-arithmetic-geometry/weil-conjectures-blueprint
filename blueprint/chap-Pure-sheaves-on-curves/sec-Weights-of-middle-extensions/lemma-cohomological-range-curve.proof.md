+++
kind = "proof"
of = "lemma-cohomological-range-curve"
order = 1184
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-pro-etale-affines-form-basis", "lemma-degree-zero-top-cohomology", "lemma-finite-quasi-finite-direct-images"]
+++
Choose a dense open $j:U\hookrightarrow C$ on which $F$ is lisse,
and let $i$ be the inclusion of the finite complement. The sequence
$0\to j_!j^*F\to F\to i_*i^*F\to0$ gives a long exact sequence in
which $H^r_c(C,i_*i^*F)$ vanishes for $r\ne0$, because the support is
finite. It therefore suffices to show $H^r_c(U,j^*F)=0$ for
$r\notin\{0,1,2\}$. For $r<0$ there is nothing to prove. For $r>2$,
degreewise Poincaré duality
(Corollary [corollary-degreewise-duality-over-fields], with $d=1$) shows
that $H^r_c(U,j^*F)$ is dual to $H^{2-r}(U,(j^*F)^\vee(1))$, which is
zero because $(j^*F)^\vee$ is a sheaf and $2-r<0$.
