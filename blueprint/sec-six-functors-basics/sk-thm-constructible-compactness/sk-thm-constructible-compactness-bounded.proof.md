+++
kind = "proof"
of = "det-constructible-compactness-bounded"
+++
Induction on $b-a$, for all $s$ simultaneously.

*$a=b$.* Then $K_\lambda\cong B_\lambda[-a]$ with $B_\lambda=H^a(K_\lambda)\in\IndCons(X,\Lambda)$, and
$\bigoplus K_\lambda\cong(\bigoplus B_\lambda)[-a]$. The map is
$\bigoplus_\lambda\Ext^{s-a}(C,B_\lambda)\to\Ext^{s-a}(C,\bigoplus B_\lambda)$, an isomorphism by
[sk-cor-ind-heart-ii].

*Induction step.* For $b>a$, the triangles

$$
\tau_{\leq b-1}K_\lambda\to K_\lambda\to H^b(K_\lambda)[-b]\to(\tau_{\leq b-1}K_\lambda)[1]
$$

have outer terms with cohomology in $[a,b-1]$ resp. $[b,b]$. A direct sum of distinguished triangles
is distinguished, and since $H^n$ commutes with direct sums ([sk-cor-ambient-ind-derived]), the sum
triangle is the truncation triangle of $\bigoplus K_\lambda$. Applying $\Hom(C,-[s])$ gives a map from
the direct sum of the long exact sequences for the $K_\lambda$ (exact, because direct sums of abelian
groups are exact) to the long exact sequence for $\bigoplus K_\lambda$. In the resulting ladder

$$
\begin{matrix}
\oplus\Hom(C,H^bK_\lambda[s-b-1])&\to&\oplus\Hom(C,\tau_{\leq b-1}K_\lambda[s])&\to&\oplus\Hom(C,K_\lambda[s])&\to&\oplus\Hom(C,H^bK_\lambda[s-b])&\to&\oplus\Hom(C,\tau_{\leq b-1}K_\lambda[s+1])\\
\downarrow&&\downarrow&&\downarrow&&\downarrow&&\downarrow\\
\Hom(C,\oplus H^bK_\lambda[s-b-1])&\to&\Hom(C,\oplus\tau_{\leq b-1}K_\lambda[s])&\to&\Hom(C,\oplus K_\lambda[s])&\to&\Hom(C,\oplus H^bK_\lambda[s-b])&\to&\Hom(C,\oplus\tau_{\leq b-1}K_\lambda[s+1])
\end{matrix}
$$

the four outer vertical maps are isomorphisms by induction, so the middle one is by the five lemma.
