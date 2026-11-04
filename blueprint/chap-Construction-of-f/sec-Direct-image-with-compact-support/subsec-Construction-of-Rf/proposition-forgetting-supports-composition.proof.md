+++
kind = "proof"
of = "proposition-forgetting-supports-composition"
order = 515
+++
All maps involved are maps out of an extension by zero, so each of them
is determined by its restriction to the open subscheme, where it is
an identity or an inverse counit. We use this repeatedly.

Independence of the compactification reduces to a refinement $h:Z'\to Z$. The two maps
$j_!K\to Rh_*Rj'_*K=Rj_*K$ obtained from
(5.7) and from $j_!K\to Rj_*K$ have the same
adjoint under $j_!\dashv j^*$, namely the inverse of $j^*Rj_*K\to K$.
Hence they are equal. Applying $Rp_*$ gives independence.

The square is checked on the compactifications that define $c^!_{g,f}$
and the interchange map (5.9). Apart from composition
and naturality squares for ordinary direct images, it comes down to
comparing the two maps

$$
j_{Y!}Rp_*M\longrightarrow Rr_*j'_!M
\longrightarrow Rr_*Rj'_*M=Rj_{Y*}Rp_*M,
\qquad
j_{Y!}Rp_*M\longrightarrow Rj_{Y*}Rp_*M.
$$

Their adjoints under $j_{Y!}\dashv j_Y^*$ are both the inverse
counit for $j_Y^*\dashv Rj_{Y*}$, because the interchange map restricts
to the identity on $Y$. So the two maps agree. Applying $Rq_*$ with $M=j_!K$,
and using naturality for $j_!K\to Rj_*K$, we get the displayed
square for the chosen compactifications. The refinement calculation
extends it to any choices. If $f$ is proper, the
compactification with $j=\mathrm{id}$ has $\eta_f$ equal to the
identity, and the last assertion follows from the square.
