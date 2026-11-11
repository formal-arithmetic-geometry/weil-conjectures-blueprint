+++
kind = "proof"
of = "lemma-fixed-point-scheme-deformation"
order = 1707
uses = ["definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-normal-cones-contracting-ideals"]
+++
Restricting $I_2^n\subset I_1^{n+1}$ to $F$, where the two legs agree,
gives $I_F^n\subset I_F^{n+1}$. The reverse inclusion always holds, so
the coherent ideal $M=I_F^n$ satisfies $M=I_FM$. Hence, at a point of
$V(I_F)$, Nakayama's lemma shows that $M=0$ in the local ring, and hence on a
neighbourhood of the point, whereas at a point outside $V(I_F)$ we have
$M=\mathcal O_F$. The closed set $V(I_F)$ is therefore also open. It is
nonempty by assumption, and $F$ is connected, so $V(I_F)=F$ and
$I_F^n=0$. This proves the first assertion.
As $I_F$ is nilpotent, each generator
$h/t$ of $\mathcal O_{F_T}[I_F/t]$ over $\mathcal O_{F_T}$ is nilpotent.
Hence the reduction of $\mathcal D_{d^{-1}(Z)}F$ is
$(F_T)_{\mathrm{red}}$.

It remains to see that $\widetilde F$ has no further points. On the
generic fibre the deformed correspondence is $c$ itself, so the
generic fibre of $\widetilde F$ is that of $F_T$. Let $x$ be a
point of the special fibre of $\widetilde F$. Then $\gamma_2(x)$ lies in
the zero section by Lemma [lemma-normal-cones-contracting-ideals](2),
and so does $\gamma_1(x)=\gamma_2(x)$. By
Lemma [lemma-normal-cones-contracting-ideals](1), the point $x$ lies on the
zero section $Z'\subset N_{Z'}C$. On $Z'$ the two maps are the restrictions
of $c_1$ and $c_2$. Their equalizer is $F\cap Z'$, whose underlying space
is $F$ by the first assertion. Thus every fixed point in the special
fibre lies in the closed subscheme above, and the closed immersion of
reduced schemes is surjective. Its ideal has zero radical and is
therefore zero, so the immersion is an isomorphism.
