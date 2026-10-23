+++
kind  = "proof"
of    = "sk-thm-wft-affine-curve-upper"
+++
The assertions in degrees other than one are [sk-l-dl-a1-endpoints].
For degree one, choose $g$ as in [sk-lem-wft-finite-map] and put
$K=g_*j_!F$. Let $W_0$ be the dense open on which $K$ is lisse and
pure. Since its complement is finite, localization
([sk-prop-sf-open-closed-triangle]) gives

$$
 H_c^1(W,K|_W)\twoheadrightarrow
 H_c^1(\mathbf A^1,K)=H_c^1(C,F).
$$

By [sk-lem-wft-infinity-reduction], after a finite extension of
the constant field there is a further surjection from $H_c^1(V,E)$
onto $H_c^1(W,K|_W)$, with $E$ pure of weight $w$ and unramified at
infinity. Let $v:V\hookrightarrow\mathbf A^1$ be the inclusion and
$i:Z\hookrightarrow\mathbf A^1$ its finite complement. The
localization sequence for $v_*E$ reads

$$
 H_c^0(Z,i^*v_*E)\longrightarrow H_c^1(V,E)
 \longrightarrow H_c^1(\mathbf A^1,v_*E)\longrightarrow0.
$$

The first group has weights at most $w$ by boundary
semicontinuity ([sk-p-real-semi]), and the last has weights at most
$w+1$ by [sk-thm-dl-a1-upper]. Hence the middle group has weights
at most $w+1$. The bound passes to its quotients under the two
surjections, and [sk-lem-wft-infinity-reduction] carries it back
to the original constant field.
