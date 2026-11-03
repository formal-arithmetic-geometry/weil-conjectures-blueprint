+++
kind = "proof"
of = "det-def-sfb-ring-object-transport"
+++
1. *Associativity.* Using naturality of $\mu^F$, then the associativity coherence of $F$, then the
   associativity of $\mu$,
   $$
   \begin{aligned}
   \mu_{FR}(\mu_{FR}\otimes FR)&=F\mu\circ\mu^F_{R,R}\circ(F\mu\otimes FR)\circ(\mu^F_{R,R}\otimes FR)
   =F\mu\circ F(\mu\otimes R)\circ\mu^F_{R\otimes R,R}\circ(\mu^F_{R,R}\otimes FR)\\
   &=F\mu\circ F(\mu\otimes R)\circ F(\alpha^{-1}_{R,R,R})\circ\mu^F_{R,R\otimes R}\circ(FR\otimes\mu^F_{R,R})\circ\alpha_{FR,FR,FR}\\
   &=F\mu\circ F(R\otimes\mu)\circ\mu^F_{R,R\otimes R}\circ(FR\otimes\mu^F_{R,R})\circ\alpha_{FR,FR,FR}
   =\mu_{FR}(FR\otimes\mu_{FR})\alpha_{FR,FR,FR}.
   \end{aligned}
   $$
   *Units.* By naturality of $\mu^F$, the left unit coherence of $F$ and the left unit law of $R$,
   $\mu_{FR}(\eta_{FR}\otimes FR)=F\mu\circ F(\eta\otimes R)\circ\mu^F_{\mathbf 1,R}\circ(\varepsilon^F\otimes FR)
   =F\mu\circ F(\eta\otimes R)\circ F(\lambda_R^{-1})\circ\lambda_{FR}=F(\lambda_R)F(\lambda_R^{-1})\lambda_{FR}=\lambda_{FR}$;
   the right unit law is symmetric. *Morphisms.* If $f\colon R\to R'$ is a morphism of ring
   objects, then $Ff\circ\mu_{FR}=F(f\mu)\mu^F_{R,R}=F(\mu'(f\otimes f))\mu^F_{R,R}=F\mu'\circ\mu^F_{R',R'}\circ(Ff\otimes Ff)$
   by naturality of $\mu^F$, and $Ff\circ\eta_{FR}=F(f\eta)\varepsilon^F=\eta_{FR'}$. Functoriality
   is that of $F$.
2. $\mu_{FR}\beta_{FR,FR}=F\mu\circ\mu^F_{R,R}\circ\beta_{FR,FR}=F\mu\circ F(\beta_{R,R})\circ\mu^F_{R,R}=F(\mu\beta_{R,R})\mu^F_{R,R}=\mu_{FR}$.
3. Monoidality of $\tau$ means $\tau_{X\otimes Y}\circ\mu^F_{X,Y}=\mu^{F'}_{X,Y}\circ(\tau_X\otimes\tau_Y)$ and
   $\tau_{\mathbf 1}\varepsilon^F=\varepsilon^{F'}$. Then
   $\tau_R\mu_{FR}=\tau_RF\mu\,\mu^F_{R,R}=F'\mu\,\tau_{R\otimes R}\mu^F_{R,R}=F'\mu\,\mu^{F'}_{R,R}(\tau_R\otimes\tau_R)=\mu_{F'R}(\tau_R\otimes\tau_R)$
   and $\tau_R\eta_{FR}=F'\eta\,\tau_{\mathbf 1}\varepsilon^F=\eta_{F'R}$, by naturality of $\tau$. If
   $\tau_R$ is invertible, its inverse is then also a morphism of ring objects.
