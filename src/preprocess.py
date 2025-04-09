import pandas as pd

def preprocess_data(filepath):
    df = pd.read_csv(filepath)
    
    # Convert IPs to numeric if needed
    df['src_ip_int'] = df['src'].apply(lambda x: sum([int(part) << (8 * i) for i, part in enumerate(reversed(x.split('.')))]))
    df['dst_ip_int'] = df['dst'].apply(lambda x: sum([int(part) << (8 * i) for i, part in enumerate(reversed(x.split('.')))]))
    
    df['protocol_code'] = df['protocol'].astype('category').cat.codes
    df = df[['src_ip_int', 'dst_ip_int', 'protocol_code', 'length']]
    return df
