+++
kind = "proof"
of = "sk-prop-b-prop-forget-supports-composition"
uses = ["sk-prop-sf-comp-coherence"]
+++
First consider a refinement $h:Z'\to Z$. The two maps
$j_!K\to Rh_*Rj'_*K=Rj_*K$ obtained from
(6.6) and from $j_!K\to Rj_*K$ have the same
adjoint under $j_!\dashv j^*$, namely the inverse of $j^*Rj_*K\to K$, so
they are equal. Applying $Rp_*$ proves independence of the
compactification.

For composition, use the compactifications that define $c^!_{g,f}$
and the interchange map (6.7). Apart from composition
and naturality squares for ordinary direct images, we must compare the
two maps

$$
j_{Y!}Rp_*M\longrightarrow Rr_*j'_!M
\longrightarrow Rr_*Rj'_*M=Rj_{Y*}Rp_*M,
\qquad
j_{Y!}Rp_*M\longrightarrow Rj_{Y*}Rp_*M.
$$

Their adjoints under $j_{Y!}\dashv j_Y^*$ are both the inverse
counit for $j_Y^*\dashv Rj_{Y*}$, because the interchange map restricts
to the identity on $Y$. Thus they agree. Apply $Rq_*$, take $M=j_!K$,
and use naturality for $j_!K\to Rj_*K$. This gives the displayed
square for the chosen compactifications. The refinement calculation
proves it for any choices. Finally, if $f$ is proper, choose the
compactification with $j=\mathrm{id}$; its map $\eta_f$ is the
identity. The last assertion follows from the square.
