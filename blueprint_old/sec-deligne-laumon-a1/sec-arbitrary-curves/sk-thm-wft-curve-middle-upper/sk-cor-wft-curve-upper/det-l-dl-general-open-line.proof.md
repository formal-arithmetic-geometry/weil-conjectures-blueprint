+++
kind  = "proof"
of    = "det-l-dl-general-open-line"
+++
After a finite constant extension, choose a rational point of $C_0$
and send it to $\infty$ by an automorphism of $\mathbf P^1$, as in
[sk-lem-wft-infinity-reduction].
Write $j:C\hookrightarrow\mathbf P^1$, $J=j_*F$ and
$H=J|_{\mathbf A^1}$. This is the ordinary middle extension from
$C\setminus\{\infty\}$, and its lisse sheaf is unramified at the new
infinity ([rem-dl-a1-conventions]). Thus [sk-thm-dl-a1-upper] applies.
Localization ([sk-prop-sf-open-closed-triangle]) gives

$$
H_c^1(\mathbf A^1,H)\twoheadrightarrow H^1(\mathbf P^1,J),
\qquad H_c^2(\mathbf A^1,H)\simeq H^2(\mathbf P^1,J).
$$

Also $H^0(\mathbf P^1,J)=H^0(C,F)$ injects into $F_{\bar\infty}$,
so has weight $w$. The finite-support quotient $B=J/j_!F$ has weights
at most $w$ by [sk-p-real-semi]. The exact sequence
$0\to j_!F\to J\to B\to0$ now gives the desired bounds: in degree
one use $H^0(B)\to H_c^1(C,F)\to H^1(\mathbf P^1,J)\to0$;
degrees zero and two follow by injection and isomorphism, respectively.
The other degrees vanish. Constant extension replaces Frobenius by a
power and reflects normalized weight bounds, so the bounds descend
([lem-a1-weight-bound-constant-extension]).
