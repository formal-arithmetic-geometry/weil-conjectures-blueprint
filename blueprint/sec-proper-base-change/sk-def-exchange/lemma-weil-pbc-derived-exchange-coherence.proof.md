+++
kind  = "proof"
of    = "lemma-weil-pbc-derived-exchange-coherence"
+++
*(1)* This is the uniqueness part of
[lemma-weil-pbc-derived-exchange-replacement]. Independence of the resolution
follows: for any bounded below injective resolution $K\to I$, naturality of
$\Ex_\square$ along the isomorphism $K\cong I$ in $\Dplus$ and the formula of
[lemma-weil-pbc-derived-exchange-replacement] for complexes of injectives
express $\Ex_{\square,K}$ through $\Ex^0_{\square,I}$, and the result is the
same morphism for every choice of $I$ since it equals $\Ex_{\square,K}$.

*Underived pasting.* We first record the pasting laws for the underived
exchange morphisms [def-weil-pbc-underived-exchange]. For vertically pasted
squares, $\Ex^0$ of the pasted square equals the composite
$k^{-1}(ef)_*\cong k^{-1}e_*f_*\xrightarrow{\Ex^0_{\square_2}}e'_*g^{-1}f_*
\xrightarrow{e'_*\Ex^0_{\square_1}}e'_*f'_*g'^{-1}\cong(e'f')_*g'^{-1}$; for
horizontally pasted squares, $\Ex^0$ of the pasted square equals
$(gh)^{-1}f_*\cong h^{-1}g^{-1}f_*\xrightarrow{h^{-1}\Ex^0_{\square_1}}
h^{-1}f'_*g'^{-1}\xrightarrow{\Ex^0_{\square_2}}f''_*g''^{-1}g'^{-1}\cong
f''_*(g'g'')^{-1}$. Indeed, expand each $\Ex^0$ as "unit, square isomorphism
$\theta$, counit". The square isomorphism of the pasted square is the composite
of the two square isomorphisms modulo composition isomorphisms
[def-weil-pbc-cartesian-square], the composition isomorphisms of direct images
are the mates of those of inverse images, and the triangle identities cancel
the adjacent unit–counit pairs; this is the compatibility of mates with
pasting.

*(3) Horizontal pasting.* By (1) it suffices to show that the displayed
composite $\Phi$ satisfies the characterizing identity of
[lemma-weil-pbc-derived-exchange-replacement] for the pasted square. Let $K$ be a
bounded below complex on $X$, and write $\eta^f$, $\eta^{f'}$, $\eta^{f''}$ for the
canonical maps from direct images to derived direct images. The composition
isomorphism $(gh)^{-1}\cong h^{-1}g^{-1}$ is natural, so it carries
$(gh)^{-1}\eta^f_K$ to $h^{-1}g^{-1}\eta^f_K$. Then $h^{-1}\Ex_{\square_1,K}\circ
h^{-1}g^{-1}\eta^f_K=h^{-1}(\eta^{f'}_{g'^{-1}K}\circ\Ex^0_{\square_1,K})$ by the
identity for $\square_1$, and
$\Ex_{\square_2,g'^{-1}K}\circ h^{-1}\eta^{f'}_{g'^{-1}K}
=\eta^{f''}_{g''^{-1}g'^{-1}K}\circ\Ex^0_{\square_2,g'^{-1}K}$ by the identity for
$\square_2$ applied to the complex $g'^{-1}K$. Finally the composition
isomorphism $g''^{-1}g'^{-1}\cong(g'g'')^{-1}$ commutes with $\eta^{f''}$ by
naturality. Altogether $\Phi_K\circ(gh)^{-1}\eta^f_K$ equals $\eta^{f''}$ composed
with the underived composite above, which is $\Ex^0$ of the pasted square
applied to $K$. So $\Phi$ is the derived exchange morphism of the pasted square.

*(2) Vertical pasting.* Again by (1) it suffices to check the characterizing
identity, and by the uniqueness argument of
[lemma-weil-pbc-derived-exchange-replacement] it suffices to check it on bounded
below complexes $I$ of injectives (every object of $\Dplus$ is isomorphic to one,
and on them the canonical maps $\eta^f_I$ are isomorphisms). For such $I$,
$f_*I$ is again a bounded below complex of injectives, because $f_*$ is right
adjoint to the exact functor $f^{-1}$; hence $\eta^f_I$, $\eta^e_{f_*I}$ and
$\eta^{ef}_I$ are isomorphisms, and the composition isomorphism
$R(ef)_*I\cong Re_*Rf_*I$ is the one induced by $(ef)_*I=e_*f_*I$. Using the
identity for $\square_2$ on the complex $f_*I$, then naturality of
$\eta^{e'}$ along the chain map $\Ex^0_{\square_1,I}$ followed by the identity for
$\square_1$ on $I$, and finally the compatibility of the composition isomorphism
$Re'_*Rf'_*\cong R(e'f')_*$ with the canonical maps
($\eta^{e'f'}_M$ corresponds to $Re'_*(\eta^{f'}_M)\circ\eta^{e'}_{f'_*M}$), the
composite of the displayed morphism with $k^{-1}\eta^{ef}_I$ becomes
$\eta^{e'f'}_{g'^{-1}I}$ composed with the underived vertical composite above,
i.e. with $\Ex^0$ of the pasted square applied to $I$. Hence the displayed
composite is the derived exchange morphism of the pasted square.
