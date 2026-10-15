+++
kind  = "proof"
of    = "sk-lem-finite"
+++
*Step 1 (finite level).* Let $\Lambda=A_{E,n}$ and let $K$ be a
bounded constructible complex of finite Tor amplitude. The structure
morphism $a_X$ is separated of finite type over the field $k$, so the
finiteness theorems for constructible sheaves apply: the sheaves $R^qa_{X,*}K$ and
$R^qa_{X,!}K$ are constructible and, if the cohomology sheaves of $K$
lie in degrees $[a,b]$, both vanish for $q\notin[a,b+2\dim X]$: the
compact-support ones by the finiteness theorem for $Ra_{X!}$ and its
comparison with the proper case, the ordinary ones by the
fibrewise cohomological-dimension bound, each applied to the
cohomology sheaves of $K$ through the spectral sequence of the truncations
(for $K=\Lambda[-1]$ on a point the bound is $1$, not $2\dim X=0$).
At the geometric point $s$ a constructible complex is a bounded complex of
finite modules, so
$\RGammac(X,K)$ and $\RGamma(X,K)$ are bounded with finite cohomology.
*Step 2 (perfectness over the Noetherian ring).* Over $A=\AEn$, a
bounded complex with finite cohomology and finite Tor amplitude is
represented by a bounded complex of finite projective modules: take a
bounded-above resolution by finitely generated free modules, truncate it in
degrees at least the lower amplitude bound, and observe that the resulting
cokernel is finitely presented of Tor-dimension zero, hence flat, hence
projective, finitely presented flat modules over a Noetherian ring being
projective.
*Step 3 (the stages and the duals).* The uniform-tower reconstruction
places $\RGammac(X,K)$ in $D^b_{\mathrm{fg}}(\Oe)$ with perfect
reductions of one common amplitude. The same holds for
$\RGamma(X,K)$: choose a compactification $j:X\hookrightarrow\bar X$
of the separated finite-type $k$-scheme $X$, as in the definition of
$Rf_!$ in [sk-def-ops]. Then
$Ra_{X*}=Ra_{\bar X*}Rj_*=Ra_{\bar X!}Rj_*$, $\bar X$ being proper,
i.e. $\RGamma(X,K)=\RGammac(\bar X,Rj_*K)$; and $Rj_*$ carries
$\Dctf(X,\Lambda)$ to $\Dctf(\bar X,\Lambda)$, with Tor amplitude
$[a,b]\mapsto[a,b+2\dim X]$, compatibly with the finite reductions
([sk-thm-sf-direct-image-tor-amplitude];
[thm-sf-ctf-stability](iii),(vii)). So $(Rj_*K_n)_n$ is again a
normalized system with common bounds on the proper $\bar X$, and the
compact-support case just proved, applied to $\bar X$ and $Rj_*K$,
places $\RGamma(X,K)$ in $D^b_{\mathrm{fg}}(\Oe)$ with perfect
reductions of one common amplitude. The rational and algebraically closed
stages of $\RGammac$ and $\RGamma$ follow by flat extension of scalars
([sk-def-ops]); the dual of a bounded complex of finite projective modules
is again one, termwise.
