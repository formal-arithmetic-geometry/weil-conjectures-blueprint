+++
id = "prose-08-03"
kind = "hidden"
title = "The remaining operations"
order = 377
+++
With $Rf_!$ and $f^!$ in place, the other four operations are a matter of
reduction to what we know. The ordinary direct image of a morphism with
a compactification $f=pj$ is $Rp_*Rj_*$, so it is controlled by proper
direct image and by the open case of
Proposition [sk-cor-sf-direct-image-ctf] and Proposition [sk-prop-open-coefficients].
Pullback and tensor product preserve the local description of
constructible complexes on strata, as $\Lambda_S\otimes P$ with $P$ perfect.
Internal Hom is the one operation where something has to be computed.
Let $a$ be the locally closed immersion of a stratum and $P$ a perfect
complex on it. For $P=\Lambda$ and $a=j$ an open immersion, the formula
$\cHom(j_!\Lambda,K)=Rj_*j^*K$ already shows that $\cHom$ involves a
nonproper direct image, and for a closed immersion $i$ the formula
$\cHom(i_*\Lambda,K)=i_*i^!K$ shows that it involves $f^!$. The general
formula $\cHom(a_!P,K)\simeq Ra_*(P^\vee\otimes^{\mathbf L}a^!K)$ combines
the two, and since every constructible complex is built from objects
$a_!P$ by finitely many cones, it reduces internal Hom to $Ra_*$, $a^!$ and
tensor products. The result, Proposition [sk-thm-sf-ctf-stability], is the form in
which the six operations are used in the rest of the notes.
