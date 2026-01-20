# Padanje v atmosferi

## Uvod

Padanje teles v atmosferi je kompleksen fizikalni pojav, ki se razlikuje od idealnega prostega pada v vakuumu. V atmosferi na padajoče telo deluje dodatna sila - upor zraka, ki bistveno vpliva na gibanje telesa.

## Teoretična podlaga

### Proste pad v vakuumu

V vakuumu na telo deluje samo gravitacijska sila:

```
F = m·g
```

kjer je:
- `m` - masa telesa [kg]
- `g` - težnostni pospešek (≈ 9.81 m/s²)

Enačba gibanja je preprosta:

```
a = g
v(t) = g·t
h(t) = h₀ - (1/2)·g·t²
```

### Padanje v atmosferi

V atmosferi na telo delujeta dve sili:
1. **Gravitacijska sila** (navzdol): `Fg = m·g`
2. **Sila upora zraka** (navzgor): `Fu`

#### Sila upora zraka

Sila upora zraka je odvisna od hitrosti in se lahko zapiše kot:

```
Fu = (1/2)·ρ·v²·Cd·A
```

kjer je:
- `ρ` - gostota zraka (≈ 1.225 kg/m³ na morski gladini)
- `v` - hitrost telesa [m/s]
- `Cd` - koeficient upora (odvisen od oblike telesa)
- `A` - prečni prerez telesa [m²]

#### Enačba gibanja

Če upoštevamo obe sili, dobimo:

```
m·a = m·g - (1/2)·ρ·v²·Cd·A
```

To je diferencialna enačba:

```
m·(dv/dt) = m·g - (1/2)·ρ·v²·Cd·A
```

### Končna hitrost (Terminal Velocity)

Ko telo dovolj dolgo pada, doseže **končno hitrost** (terminal velocity) `vk`, pri kateri je sila upora enaka gravitacijski sili:

```
m·g = (1/2)·ρ·vk²·Cd·A
```

Končna hitrost je torej:

```
vk = √(2·m·g / (ρ·Cd·A))
```

## Primeri končnih hitrosti

| Objekt | Končna hitrost |
|--------|----------------|
| Padalec (razprt) | 50-60 m/s (180-220 km/h) |
| Padalec (ptica) | 90 m/s (320 km/h) |
| Kapljica dežja (5mm) | 9 m/s (32 km/h) |
| Človeško telo | 53 m/s (190 km/h) |
| Toča (5cm) | 40 m/s (144 km/h) |

## Koeficienti upora (Cd)

Koeficient upora je odvisen od oblike telesa:

| Oblika | Cd |
|--------|-----|
| Krogla | 0.47 |
| Polkrogla (votla stran naprej) | 1.42 |
| Polkrogla (okrogla stran naprej) | 0.42 |
| Stožec (vrh naprej) | 0.50 |
| Kocka | 1.05 |
| Aerodinamično telo | 0.04-0.10 |
| Padalec (razprt) | 1.0-1.3 |
| Padalec (ptica) | 0.7 |

## Reynoldsovo število

Reynoldsovo število določa naravo toka okoli telesa:

```
Re = (ρ·v·L) / μ
```

kjer je:
- `L` - karakteristična dolžina telesa [m]
- `μ` - dinamična viskoznost zraka (≈ 1.81×10⁻⁵ Pa·s)

- **Re < 1**: Laminarni tok, Stokesov upor (Fu ∝ v)
- **1 < Re < 10⁵**: Prehodno področje
- **Re > 10⁵**: Turbuletni tok (Fu ∝ v²)

## Numerična rešitev

Enačbo gibanja z uporom zraka lahko rešimo numerično z Eulerjevo metodo:

```python
import numpy as np
import matplotlib.pyplot as plt

# Parametri
m = 70.0        # masa [kg]
g = 9.81        # težnostni pospešek [m/s²]
rho = 1.225     # gostota zraka [kg/m³]
Cd = 1.0        # koeficient upora
A = 0.7         # površina prečnega prereza [m²]

# Začetni pogoji
v0 = 0.0        # začetna hitrost [m/s]
h0 = 4000.0     # začetna višina [m]

# Časovni korak
dt = 0.1        # [s]
t_max = 60.0    # [s]

# Časovni vektor
t = np.arange(0, t_max, dt)
n = len(t)

# Inicializacija
v = np.zeros(n)
h = np.zeros(n)
v[0] = v0
h[0] = h0

# Eulerjeva metoda
for i in range(n-1):
    Fu = 0.5 * rho * v[i]**2 * Cd * A
    a = g - Fu/m
    v[i+1] = v[i] + a * dt
    h[i+1] = h[i] - v[i] * dt
    
    # Ustavimo se, ko dosežemo tla
    if h[i+1] <= 0:
        h[i+1] = 0
        v[i+1] = 0
        break

# Izračun končne hitrosti (teoretično)
v_terminal = np.sqrt(2 * m * g / (rho * Cd * A))
print(f"Končna hitrost (teoretično): {v_terminal:.2f} m/s")
print(f"Končna hitrost (numerično): {max(v):.2f} m/s")

# Grafični prikaz
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t[:i+2], v[:i+2])
plt.axhline(y=v_terminal, color='r', linestyle='--', label='Končna hitrost')
plt.xlabel('Čas [s]')
plt.ylabel('Hitrost [m/s]')
plt.title('Hitrost v odvisnosti od časa')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t[:i+2], h[:i+2])
plt.xlabel('Čas [s]')
plt.ylabel('Višina [m]')
plt.title('Višina v odvisnosti od časa')
plt.grid(True)

plt.tight_layout()
plt.show()
```

## Aplikacije in zanimivosti

### 1. Padalstvo

Padalci izkoriščajo upor zraka za varno pristajanje. S spremembo drže telesa lahko nadzorujejo hitrost:
- **Razprt položaj**: večja površina → večji upor → manjša hitrost (50-60 m/s)
- **Položaj "ptice"**: manjša površina → manjši upor → večja hitrost (90+ m/s)

### 2. Felix Baumgartner - Red Bull Stratos

Leta 2012 je Felix Baumgartner skočil iz višine 39 km:
- Dosegel je hitrost 1.357,6 km/h (377,1 m/s)
- Presegel je zvočno bariero v prostem padu
- Na velikih višinah je zrak redek, zato je upor manjši

### 3. Meteoriti

Meteoriti v atmosferi dosegajo ogromne hitrosti (10-70 km/s). Upor zraka povzroči:
- Segrevanje meteoritov (plazma)
- Upočasnitev
- Razpad manjših meteorov

### 4. Deževne kaplje

Brez upora zraka bi deževne kaplje padale s hitrostjo preko 100 m/s in bi bile nevarne. Upor zraka jih upočasni na ~9 m/s.

## Vpliv višine na gostoto zraka

Gostota zraka pada z višino po približni enačbi:

```
ρ(h) = ρ₀ · e^(-h/H)
```

kjer je:
- `ρ₀` - gostota na morski gladini (1.225 kg/m³)
- `H` - višinska lestvica (≈ 8500 m)
- `h` - višina nad morsko gladino [m]

To pomeni, da je upor zraka na večjih višinah manjši, kar omogoča višje hitrosti.

## Zaključek

Padanje v atmosferi je zapleten pojav, ki ga določa ravnovesje med gravitacijo in uporom zraka. Razumevanje tega pojava je pomembno za:
- Varnost v letalstvu in padalstvu
- Napovedovanje vremena (padanje dežnih kapljic)
- Vesoljske tehnologije (vračanje satelitov)
- Študij meteorov

Čeprav je matematični opis kompleksen, lahko s preprostimi numeričnimi metodami dobimo dobre približke za realne situacije.

## Literatura in viri

1. Halliday, D., Resnick, R., & Walker, J. (2013). Fundamentals of Physics. Wiley.
2. Serway, R. A., & Jewett, J. W. (2018). Physics for Scientists and Engineers. Cengage Learning.
3. NASA - Terminal Velocity: https://www.grc.nasa.gov/www/k-12/airplane/termv.html
4. Red Bull Stratos - Mission Data: https://www.redbullstratos.com/
